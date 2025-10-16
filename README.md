# vllm-edge
The edge-based vLLM framework, which is suitable for devices with limited video memory, low communication bandwidth, and weak computing ability.

## install
```shell
git clone https://github.com/JingliangGao/vllm-edge.git
cd vllm-edge/
chmod +x ./build-for-debug.sh && ./build-for-debug.sh
```

## download model    
```shell
modelscope download --model Qwen/Qwen3-0.6B
```


## run     
```shell
cd vllm_edge/examples/
python3  qwen3_inference.py
```