# austinrockman/reflector

⭐ 26 · Python · Apache-2.0 · 推送 2026-08-11 · [GitHub](https://github.com/austinrockman/reflector) · [官网](https://austinrockman.com/) · 个人维护

**为音乐制作人提供样本库和声检索的本地音频工作站**

面向样本作曲的 macOS 交互式音频工作站：用训练好的两塔编码器学习样本库的和声结构，将音频嵌入 128 维向量，以点积实时检索与当前编曲和声相容的样本；编码器由手工设计的 12×12 音级核函数作为 oracle，在合成音频数据上蒸馏训练，训练数据全部合成、无版权音频。应用完全本地运行，仅支持 Apple Silicon；仓库另提供完整训练管线，可用 mps/cuda/cpu 复现编码器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两塔编码器将 3 秒 chroma 窗口嵌入为 128 维单位向量，点积实现交互式检索
- 训练数据全部为合成音频，oracle 为手工设计的音级区间核函数
- 免费签名 macOS 应用，全部功能本地运行，仅支持 Apple Silicon
- 仓库包含完整训练管线，--device 支持 mps/cuda/cpu

## 适用场景

- 在大型自有样本库中实时查找与当前编曲和声相合的样本
- 跨会话与不同编曲持续检索自己的声音库
- 复现或研究其检索模型的训练流程

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L13: Reflector is an interactive audio workstation that automates and inspires the process of sample-based composition b
> L23: and unpublished. Reflector is an experimental take on the same idea for your personal library: it searches
> L36: Reflector runs entirely on your machine as a free, signed macOS application.

## 星数曲线

```mermaid
xychart-beta
    title "austinrockman/reflector 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-30 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6491502d2cd1` · [字段定义](../../DATASET.md)*
