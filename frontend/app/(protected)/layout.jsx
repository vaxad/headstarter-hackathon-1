import PhoneOverlay from "@/components/custom-ui/PhoneOverlay";


export default function RootLayout({ children }) {
    return (
        <>
            <PhoneOverlay />
            {children}
        </>
    );
}
