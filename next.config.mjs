import createMDX from '@next/mdx';
import createNextIntlPlugin from 'next-intl/plugin';
import remarkGfm from 'remark-gfm';
import rehypeSlug from 'rehype-slug';

function rehypeUndisableCheckboxes() {
  return (tree) => {
    const visit = (node) => {
      if (node.type === 'element') {
        if (node.tagName === 'input' && node.properties?.type === 'checkbox') {
          delete node.properties.disabled;
        }
      }
      if (node.children) {
        node.children.forEach(visit);
      }
    };
    visit(tree);
  };
}

const withMDX = createMDX({
  extension: /\.mdx?$/,
  options: {
    remarkPlugins: [remarkGfm],
    rehypePlugins: [rehypeSlug, rehypeUndisableCheckboxes],
  },
});

const withNextIntl = createNextIntlPlugin('./src/i18n/request.ts');

/** @type {import('next').NextConfig} */
const nextConfig = {
  output: process.env.NODE_ENV === 'production' ? 'export' : undefined,
  trailingSlash: true,
  pageExtensions: ['js', 'jsx', 'md', 'mdx', 'ts', 'tsx'],
  images: {
    unoptimized: true,
  },
  env: {
    NEXT_PUBLIC_GA_ID: 'G-LC9021XYBB',
    NEXT_PUBLIC_CLOUDFLARE_ZONE_ID: '400c73d67260aa25b61c9b1f232d7c17',
  },
};

export default withNextIntl(withMDX(nextConfig));
