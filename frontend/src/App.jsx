import React, { useState } from 'react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import RemediationForm from './components/RemediationForm';
import StatusView from './components/StatusView';
import { Shield } from 'lucide-react';

const queryClient = new QueryClient();

function App() {
    const [workflowId, setWorkflowId] = useState(null);

    return (
        <QueryClientProvider client={queryClient}>
            <div className="min-h-screen bg-gray-900 text-gray-100 p-8 font-sans">
                <header className="max-w-4xl mx-auto mb-8 flex items-center justify-between border-b border-gray-700 pb-4">
                    <div className="flex items-center gap-3">
                        <Shield className="text-green-500 w-10 h-10" />
                        <div>
                            <h1 className="text-3xl font-bold tracking-tighter text-white">SENTINEL_CODE</h1>
                            <p className="text-xs text-gray-500 uppercase tracking-widest">Automated Vulnerability Remediation System</p>
                        </div>
                    </div>
                    <div className="text-right">
                        <div className="inline-block px-2 py-1 bg-green-900/30 text-green-400 text-xs rounded border border-green-800">
                            SYSTEM ONLINE
                        </div>
                    </div>
                </header>

                <main className="max-w-4xl mx-auto space-y-8">
                    {!workflowId ? (
                        <RemediationForm onStart={setWorkflowId} />
                    ) : (
                        <div className="space-y-6">
                            <button
                                onClick={() => setWorkflowId(null)}
                                className="text-sm text-green-400 hover:text-green-300 underline"
                            >
                                ← Return to Mission Control
                            </button>
                            <StatusView workflowId={workflowId} />
                        </div>
                    )}
                </main>
            </div>
        </QueryClientProvider>
    );
}

export default App;
