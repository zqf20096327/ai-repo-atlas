# Tencent/AngelSlim

⭐ 1,830 · Python · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/Tencent/AngelSlim) · [官网](https://angelslim.readthedocs.io) · 组织维护 · 中文 README

**大模型压缩工具包：量化/投机解码/蒸馏/剪枝统一框架**

腾讯开源的大模型压缩工具包，将主流压缩算法整合为统一框架，覆盖量化（FP8/INT4/NVFP4/低比特）、投机解码（DFly/MTP/Eagle3/DFlare 等）、稀疏注意力、蒸馏与 VLM 视觉 token 剪枝。支持 LLM、VLM、扩散模型与语音模型四类场景，通过配置文件一键运行压缩流程，并发布多款 Hunyuan 系列压缩后模型权重。以 pip 包提供，投机解码训练框架 AngelSpec 作为 git 子模块集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 量化算法覆盖 FP8/INT8/INT4/NVFP4/1.25-bit 等多种方案
- 投机解码训练支持 DFly、MTP、Eagle3 等多种 draft 方法
- 场景覆盖 LLM/VLM、扩散模型与语音模型（TTS/ASR）
- 通过 YAML 配置一键运行压缩流程，附 Python Engine API

## 适用场景

- 对 Hunyuan/Qwen/DeepSeek 等模型做 FP8 或 INT4 量化后部署
- 训练投机解码 draft 模型以提升推理吞吐
- 对扩散模型做量化并直接运行推理验证
- 对 VLM 做视觉 token 剪枝降低长上下文开销

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L5: A more accessible, comprehensive, and efficient toolkit for large model compression.
> L43: - **Highly Integrated**: This toolkit integrates mainstream compression algorithms into a unified framework, offeri
> L213: python3 tools/run.py -c configs/qwen3/fp8_static/qwen3-1_7b_fp8_static.yaml

## 星数曲线

```mermaid
xychart-beta
    title "Tencent/AngelSlim 星数(近 22 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 1764 --> 1836
    line [1770, 1771, 1773, 1775, 1777, 1778, 1779, 1780, 1779, 1771, 1786, 1788, 1789, 1792, 1793, 1800, 1804, 1809, 1811, 1812, 1813, 1830]
```

2026-10-24 1,770 → 2026-11-26 1,830（+60）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `d5a27f13a6ed` · [字段定义](../../DATASET.md)*
