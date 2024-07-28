
export default function PhoneOverlay() {
    return (
        <div className=' md:hidden flex fixed top-0 right-0 w-full h-full p-4 bg-background text-foreground'>
            <div className='flex flex-col gap-4 w-screen h-screen p-4 justify-center '>
                <h1 className='text-3xl font-bold'>Mobile View</h1>
                <p className='text-lg'>This app is not optimized for mobile view. Please use a desktop browser for the best experience.</p>
            </div>
        </div>
    )
}
