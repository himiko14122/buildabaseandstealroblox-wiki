import './globals.css';
import JsonLd from '@/components/JsonLd';
import { organizationJsonLd, websiteJsonLd, videoGameJsonLd } from '@/lib/seo';

const SITE_WIDE_JSONLD = {
  '@context': 'https://schema.org',
  '@graph': [
    organizationJsonLd(),
    websiteJsonLd(),
    videoGameJsonLd(),
  ],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <>
      <JsonLd data={SITE_WIDE_JSONLD} />
      {children}
    </>
  );
}
