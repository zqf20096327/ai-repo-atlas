# sfxnz/GLM-5.3-Flash-NVFP4-vLLM-2x-DGX-Spark

⭐ 21 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/sfxnz/GLM-5.3-Flash-NVFP4-vLLM-2x-DGX-Spark) · 组织维护

**在 2× DGX Spark 上以 vLLM 部署 GLM-5.3-Flash NVFP4 的配置方案**

面向双 NVIDIA DGX Spark（GB10）节点的模型部署配方：以打过补丁的 vLLM 镜像链（v8-v13 Dockerfile）在张量并行 2 下服务 GLM-5.3-Flash NVFP4 量化模型（320B/18B 激活，约 190.5 GiB），默认启用 DFlash2 块扩散投机解码（7 个投机 token、双序列），服务 327,680 上下文。通过 NVFP4 drafter、INT8 目标组、自适应验证等开关调优吞吐，给出解码基准、质量分层验证与证据文件。需两节点 QSFP RoCE 互联、Docker 与 NVIDIA Container Toolkit，每节点约 220 GiB 磁盘。附带权衡：长上下文 prefill 慢约 10.5%；DFlash2 草稿模型为 CC BY-NC-ND 4.0 许可（商用需另授权）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- v8-v13 Dockerfile 镜像链逐步叠加 sm_121 补丁、DFlash2 支持与运行时补丁
- DFlash2 块扩散投机解码默认 7 个投机 token，贪婪输出与 MTP 逐字节一致
- 每个调优开关（JIT 缓存、NVFP4 drafter、INT8 目标组、自适应验证）均有独立启动与证据文件记录
- run.sh 校验双节点镜像一致性、拒绝不安全配置（MTP on nvidia pack、stock 镜像 tag）

## 适用场景

- 在两台 DGX Spark 上跑起 GLM-5.3-Flash 长上下文推理服务
- 复现解码基准与质量验证流程
- 在 MTP 与 DFlash2 投机解码之间切换并回滚

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Serve nvidia/GLM-5.3-Flash-NVFP4 across two NVIDIA DGX Spark (GB10) nodes at tensor-parallel 2.
> L7: Stock `vllm/vllm-openai:glm53-flash-arm64-cu130` loads on sm_121 and echoes the prompt. Build the local image chain 
> L85: The v8 Dockerfile starts from `vllm/vllm-openai:glm53-flash-arm64-cu130` and applies the sm_121 patches (NoPE FA2 b

## 星数曲线

```mermaid
xychart-beta
    title "sfxnz/GLM-5.3-Flash-NVFP4-vLLM-2x-DGX-Spark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `92a66f7193d9` · [字段定义](../../DATASET.md)*
