// esbuild configuration for bir_ph_jmit
// This is a backend-only app with no frontend assets to build

module.exports = {
  // Skip building for this app
  skip: true,
  
  // No entry points
  entryPoints: [],
  
  // No output
  outdir: '',
  
  // Backend-only flag
  backend_only: true
};