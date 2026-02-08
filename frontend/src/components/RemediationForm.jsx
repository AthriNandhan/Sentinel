import React, { useState } from 'react';
import { startRemediation } from '../services/api';
import { Play, Loader2 } from 'lucide-react';

const RemediationForm = ({ onStart }) => {
    const [codePath, setCodePath] = useState('');
    const [vulnType, setVulnType] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');
        try {
            const data = await startRemediation(codePath, vulnType);
            onStart(data.workflow_id);
        } catch (err) {
            const errorMessage = err.response?.data?.detail || 'Failed to start remediation. Check console for details.';
            setError(typeof errorMessage === 'string' ? errorMessage : JSON.stringify(errorMessage));
            console.error("Remediation Error:", err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="bg-gray-800 p-6 rounded-lg shadow-lg border border-gray-700">
            <h2 className="text-xl font-bold mb-4 text-green-400 flex items-center gap-2">
                <Play size={20} /> Start New Mission
            </h2>
            <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                    <label className="block text-sm font-medium text-gray-400">Target File Path</label>
                    <input
                        type="text"
                        value={codePath}
                        onChange={(e) => setCodePath(e.target.value)}
                        className="mt-1 block w-full bg-gray-900 border border-gray-600 rounded-md shadow-sm py-2 px-3 text-white focus:outline-none focus:ring-green-500 focus:border-green-500"
                        placeholder="C:/Projects/vulnerable.py"
                        required
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-400">Vulnerability Type</label>
                    <select
                        value={vulnType}
                        onChange={(e) => setVulnType(e.target.value)}
                        className="mt-1 block w-full bg-gray-900 border border-gray-600 rounded-md shadow-sm py-2 px-3 text-white focus:outline-none focus:ring-green-500 focus:border-green-500"
                        required
                    >
                        <option value="" disabled>Select Vulnerability Type</option>
                        <option value="SQL Injection">SQL Injection</option>
                        <option value="XSS (Cross-Site Scripting)">XSS (Cross-Site Scripting)</option>
                        <option value="RCE (Remote Code Execution)">RCE (Remote Code Execution)</option>
                        <option value="Path Traversal">Path Traversal</option>
                        <option value="Insecure Deserialization">Insecure Deserialization</option>
                        <option value="Hardcoded Credentials">Hardcoded Credentials</option>
                        <option value="Buffer Overflow">Buffer Overflow</option>
                        <option value="Race Condition">Race Condition</option>
                    </select>
                </div>
                {error && <p className="text-red-500 text-sm">{error}</p>}
                <button
                    type="submit"
                    disabled={loading}
                    className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-black bg-green-500 hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 disabled:opacity-50"
                >
                    {loading ? <Loader2 className="animate-spin" /> : 'Launch Sentinel'}
                </button>
            </form>
        </div>
    );
};

export default RemediationForm;
