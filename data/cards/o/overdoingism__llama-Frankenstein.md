# overdoingism/llama-Frankenstein

⭐ 3 · PowerShell · MIT · 推送 2026-11-21 · [GitHub](https://github.com/overdoingism/llama-Frankenstein) · 个人维护 · 中文 README

**AMD RDNA4 GPU 上 llama.cpp 推理的优化补丁集**

为 llama-cpp-rdna-boosts 提供的补丁集合，面向 AMD RDNA4（gfx1201，Radeon AI PRO R9700）：按推理流程编号为 J1-J7 七组补丁，涉及 fp8 prefill 注意力与 GEMM、GPU 驻留的投机解码管线、KV 缓存与请求间状态管理等。仅发布补丁文件（MIT），不发布二进制；README 记录性能数字（Qwen3.8-27B 上的 prefill/decode 吞吐与 KLD 对照）、复现条件、构建步骤与各开关的环境变量。仅测试于 gfx1201。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七组补丁（J1-J7）覆盖 attention、prefill、decode/verify、sampling、投机解码、step issue 与请求间状态
- fp8 prefill 路径经 hipBLASLt，支持 K-quant 与 MXFP4 权重
- 每个部分有独立环境变量开关，FRANK_ALL=0 可关闭全部改变数值的部分
- README 给出完整复现条件（pinned 源码、构建、命令与 KLD 测量方法）

## 适用场景

- 在 Radeon AI PRO R9700 上以补丁方式加速 llama.cpp 本地推理
- 复现 README 中的 RDNA4 性能与 KLD 测量结果
- 以开关方式逐组启用/关闭各项优化

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L4: R9700). They sew techniques from published papers onto llama.cpp and rdna-boosts, a body sewn together from the part
> L110: HSA_USERPTR_FOR_PAGED_MEM=0 ./llama-server -m Qwen3.8-27B-UD-Q5_K_M.gguf -ngl 99 -c 131072 --kv-unified \
> L92: |ROCm|10.0.0 with hipBLASLt, the HIP code compiled for gfx1201|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `9ddd1949f4de` · [字段定义](../../DATASET.md)*
