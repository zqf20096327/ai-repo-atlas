# Gremble-io/Detto

⭐ 521 · Swift · NOASSERTION · 推送 2026-07-22 · [GitHub](https://github.com/Gremble-io/Detto) · [官网](https://detto.app) · 个人维护

**macOS 本地会议转录/语音备忘/全局听写的桌面应用**

面向 Apple Silicon Mac 的本地语音捕获应用：会议录音（麦克风与系统音频分轨标注说话人）、语音备忘、按住热键的系统级听写。ASR 经 Parakeet-TDT v3 运行于 Neural Engine，文本经 MLX 运行的 Llama 3.2 3B（4-bit）在 GPU 上本地润色；首次下载模型后不再有网络活动，无账户无服务器。输出为带 YAML frontmatter 的 markdown 文件，可指向 Obsidian vault，读取客户文件生成通话前简报。限制：仅 Apple Silicon、macOS 26+，润色仅英文调优，单用户无团队功能。以 BSL 1.1 发布（2030 年自动转 MIT）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Parakeet-TDT v3 ASR + MLX 运行的 Llama 3.2 3B 全本地推理
- 麦克风/系统音频分轨说话人分离，检测 Teams/Zoom/Slack 等 conferencing 应用
- 输出带 YAML frontmatter 的 markdown，读取 vault 客户文件生成通话前简报
- 25 种欧洲语言自动检测，不保存音频、默认对屏幕共享隐藏

## 适用场景

- 通话时自动转录并以结构化 markdown 存入 Obsidian vault
- 按住热键在任何应用内做离线全局听写
- 通话前查看客户联系人、优先事项的简报面板

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L11: Detto is a macOS app for Apple Silicon. It captures meetings, takes voice memos, and gives you system-wide dictatio
> L33: **On-device intelligence.** ASR runs on the Apple Neural Engine via Parakeet-TDT v3. Text refinement runs on the GP

## 星数曲线

```mermaid
xychart-beta
    title "Gremble-io/Detto 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 518 --> 522
    line [519, 521, 521]
```

2026-10-18 519 → 2026-10-31 521（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `fbb4f0f352ad` · [字段定义](../../DATASET.md)*
