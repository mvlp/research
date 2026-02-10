export default async (req, res) => {
  const { reqHandler } = await import('../dist/research/server/server.mjs');
  return reqHandler(req, res);
};
