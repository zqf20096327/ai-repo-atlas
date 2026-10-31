# Leo6Leo/whispr-stream

⭐ 21 · Swift · MIT · 推送 2026-10-16 · [GitHub](https://github.com/Leo6Leo/whispr-stream) · [官网](https://leo6leo.github.io/whispr-stream/) · 个人维护

**macOS 本地流式语音听写应用，基于 Qwen3-ASR/MLX**

面向 Apple silicon Mac 的开源听写应用：按住快捷键说话，转写文本插入光标处，可用于任意应用。内置 Qwen3-ASR 模型经 MLX 本地运行，无账号、服务器或音频上传。支持句中混合多语言切换、自定义词汇、语音快捷短语展开；对非流式模型通过反复重读增量语句并固定稳定词实现实时预览。Swift 前端与 Python ASR sidecar 以换行分隔 JSON 协议本地通信。需 macOS 14+、约 4 GB 空间；实验性模型适配在编译期开关后，未包含于公开 1.0.3 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地运行 Qwen3-ASR（0.6B/1.7B 经 MLX），无音频上传
- 句中多语言混合切换听写
- 自定义词汇与语音快捷短语展开
- 非流式模型通过重读增量语句生成实时预览

## 适用场景

- 在笔记、邮件、终端或编码代理中用语音输入文字
- 混合语言（不限于中英）场景下边说边写
- 本地离线语音听写，不依赖云服务

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L9: WhisprStream is an open-source macOS dictation app that types at your cursor while you speak. It runs locally, keeps
> L44: 4. Choose a speech model. Qwen3-ASR 0.6B is the recommended download at approximately 1.9 GB. Qwen3-ASR 1.7B is app
> L85: WhisprStream is MIT licensed and designed to be inspected, adapted, and extended. The public 1.0.3 app offers the b

## 星数曲线

```mermaid
xychart-beta
    title "Leo6Leo/whispr-stream 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b0e93c42c864` · [字段定义](../../DATASET.md)*
