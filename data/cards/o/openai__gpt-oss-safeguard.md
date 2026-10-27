# openai/gpt-oss-safeguard

⭐ 62 · Apache-2.0 · 推送 2026-01-14 · [GitHub](https://github.com/openai/gpt-oss-safeguard) · 组织维护

**基于 gpt-oss 的安全分类与安全推理开源模型（120B/20B）**

OpenAI 发布的两个安全推理模型 gpt-oss-safeguard-120b 与 gpt-oss-safeguard-20b，基于 gpt-oss 构建，可按用户提供的自定义安全策略对文本内容进行分类，并执行一组基础安全任务。120B 版面向可在单张 80GB GPU（如 NVIDIA H100、AMD MI300X）上运行的生产场景；20B 版面向低延迟与本地/专用场景。模型须配合 harmony 响应格式使用，否则无法正确工作；提供推理示例、提示指南、示例策略与黄金集，权重可从 Hugging Face Hub 下载，采用 Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按自定义安全策略对文本内容进行安全分类
- 120B 版（5.1B 激活参数）适配单张 80GB GPU；20B 版面向低延迟/本地场景
- 输出包含完整推理过程，可配置 low/medium/high 推理强度
- Apache 2.0 许可，权重托管于 Hugging Face Hub

## 适用场景

- 按自有安全策略对线上内容做安全分类
- 在本地或专用低延迟场景运行内容安全检测
- 调试与审计安全判定背后的推理过程

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L10: `gpt-oss-safeguard-120b` and `gpt-oss-safeguard-20b` are safety reasoning models built-upon gpt-oss.
> L11: With these models, you can classify text content based on safety policies that you provide and perform a suite of f

## 星数曲线

```mermaid
xychart-beta
    title "openai/gpt-oss-safeguard 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 60 --> 63
    line [61, 62, 62]
```

2026-10-18 61 → 2026-10-27 62（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `67864df455e9` · [字段定义](../../DATASET.md)*
