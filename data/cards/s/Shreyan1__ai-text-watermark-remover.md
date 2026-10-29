# Shreyan1/ai-text-watermark-remover

⭐ 19 · Python · 推送 2026-08-16 · [GitHub](https://github.com/Shreyan1/ai-text-watermark-remover) · 个人维护

**本地去除 AI 文本水印（SynthID-Text/KGW/Unigram）的命令行工具**

通过从语义表示重建 token 序列来去除统计文本水印，方案无关（scheme-blind），全程使用本地开源权重模型。确定性核心（元数据剥离、字符清洗、评分、事实检查）仅需标准库、无需网络；改写阶段经本地 Ollama 调用白名单模型（默认 gemma3:4b），并带语义守卫与事实门控。仅在 macOS（Apple silicon）测试；拒绝承诺不可测的『完全不可检测』。提供 reweave CLI 与可复现基准脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于语义再生的水印去除，方案无关（TPR 1.000→0.000）
- 确定性核心零依赖、离线运行，禁用网络套件测试保证
- 本地 Ollama 白名单模型改写，托管端点被直接拒绝
- 语义守卫（嵌入）+ 事实门控（规则+NLI）保持原意与事实

## 适用场景

- 去除本地已测量水印的 AI 文本以便合规检测
- 剥离聊天下载文件中的来源 URL 与生成器标签
- 重写 AI 风格文本并校验事实未丢失

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: **Remove statistical text watermarks (SynthID-Text, KGW, Unigram) by rebuilding
> L8: Watermark removal here is a side effect, not a trick. The system regenerates the
> L74: |`reweave facts --nli`, `fix --regenerate`|local Ollama|a local open-weight model, never hosted|

## 星数曲线

```mermaid
xychart-beta
    title "Shreyan1/ai-text-watermark-remover 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27", "2026-10-29"]
    y-axis "stars" 15 --> 20
    line [16, 17, 19, 19]
```

2026-10-18 16 → 2026-10-29 19（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `01a9a7db6e61` · [字段定义](../../DATASET.md)*
