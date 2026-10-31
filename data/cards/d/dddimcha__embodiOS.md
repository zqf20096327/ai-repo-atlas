# dddimcha/embodiOS

⭐ 13 · C · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/dddimcha/embodiOS) · 个人维护

**裸机内核内嵌量化 LLM：模型即操作系统的 x86_64/aarch64 单文件**

embodiOS 是一个 bare-metal x86_64 与 aarch64 内核，将量化 LLM（GGUF）直接链接进单个 embodios.elf：无 Linux、无 libc、无依赖，以 QEMU 内核、ISO 或 USB 启动后进入串口/HDMI 控制台的 LLM 对话。自研推理栈含 GGUF 解析、BPE 分词、RoPE/GQA、KV cache、Q2_K–Q6_K 等量化与 Vulkan 计算路径，K-quant 与 llama.cpp 逐位一致。支持 SMP 并行推理、exo 式 UDP 发现的分布式分片推理及 OpenAI 兼容 API。目标场景含假肢设备等实时控制（1 kHz PID 环 + LLM 策略钩子）；树莓派真机验证仍是待完成事项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 单二进制含内核+驱动+推理栈，QEMU/ISO/USB/UEFI/树莓派多方式启动
- GGUF/BPE/RoPE/GQA/KV cache 全 freestanding C 实现，量化格式 Q2_K–Q6_K 与 ggml 逐位移植
- exo 式分布式推理：UDP 发现组环、按内存分片、OpenAI 兼容 API
- 1 kHz 实时 PID 电机环带异步 LLM 策略钩子

## 适用场景

- 在无操作系统的裸机或嵌入式设备上直接运行 LLM 推理
- 学习从引导加载到 transformer logits 的完整实现路径
- 在树莓派等单板机上搭建 LLM+实时控制的机器人/假肢原型
- 多节点分布式分片运行量化模型并对外提供 OpenAI 兼容接口

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: `embodios.elf` is a bare-metal x86_64 **and aarch64** kernel with a quantized LLM compiled
> L8: with a transformer running on raw hardware. No Linux. No libc. No userspace.
> L25: ./embodi run           # boot in QEMU — you're chatting with an LLM on bare metal

## 星数曲线

```mermaid
xychart-beta
    title "dddimcha/embodiOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `660eaefa1f99` · [字段定义](../../DATASET.md)*
