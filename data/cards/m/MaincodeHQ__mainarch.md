# MaincodeHQ/mainarch

⭐ 25 · Rust · Apache-2.0 · 推送 2026-08-15 · [GitHub](https://github.com/MaincodeHQ/mainarch) · 组织维护

**从零编写的 AMD GPU Rust 推理栈：绕过 ROCm 直连内核驱动**

用 Rust 从 ABI 层向上构建的 LLM 推理栈：直接打开 /dev/kfd、手写 ioctl 与 AQL 派发包，不加载 ROCm/HIP/HSA 运行时。覆盖 GPU 虚拟内存、代码对象加载、XGMI 集合通信、FlashDecoding 注意力、解码层与 SafeTensors 权重加载，可在 MI355X（gfx950）上运行 OLMo 2 并提供 /v1/chat/completions 服务。自述为参考架构与原型，非 ROCm/vLLM/SGLang 的生产替代；无 GPU 时可用 CPU 模拟通道与脚本化演示页。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 直接对 amdkfd/amdgpu 内核 ABI 发 ioctl，运行时不加载任何 ROCm 组件
- 在 MI355X 上运行 OLMo 2 并提供 OpenAI 形状的 /v1/chat/completions
- 无 GPU 环境可运行 CPU 通道：ELF 代码对象解析、模拟器集合通信测试与演示页
- 各层为独立 crate，数值对 f64 参考实现校验，all-reduce 对 CPU oracle 位精确

## 适用场景

- 研究 AMD GPU 从内核 ABI 到推理服务的完整栈结构
- 在 MI355X（gfx950）上直接运行 OLMo 2 模型
- 在无 GPU 的 Linux 主机上阅读与实验底层 GPU 推理组件

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L17: mainarch skips them. It opens `/dev/kfd`, builds the dispatch packet by hand,
> L34: That completion came out of `/v1/chat/completions` on an MI355X, from weights
> L40: production replacement for ROCm, vLLM, or SGLang, and the

## 星数曲线

```mermaid
xychart-beta
    title "MaincodeHQ/mainarch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-28 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ce9552365ca2` · [字段定义](../../DATASET.md)*
