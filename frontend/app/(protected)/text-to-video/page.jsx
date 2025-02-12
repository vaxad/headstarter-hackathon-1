
export default function Page() {
  return (
    <div className=' flex flex-col justify-start items-center min-h-[90vh] p-8'>
      <div className={"flex flex-col gap-4 w-full"}>
        <div className={"flex flex-row gap-4 items-center w-full"}>

          <span className={"text-3xl font-bold"}>
            {`Convert your Text to Video`}
          </span>
        </div>
        <hr />
        <iframe
          src="https://ali-vilab-modelscope-text-to-video-synthesis.hf.space"
          frameborder="0"
          className=' w-full min-h-[70vh]'
        ></iframe>
      </div>
    </div>
  )
}
