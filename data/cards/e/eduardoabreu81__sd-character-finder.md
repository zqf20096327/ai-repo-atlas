# eduardoabreu81/sd-character-finder

⭐ 18 · Python · MIT · 推送 2026-11-16 · [GitHub](https://github.com/eduardoabreu81/sd-character-finder) · 个人维护

**SD WebUI 扩展：离线浏览 39,006 个角色标签与 19,800+ 画师风格**

Stable Diffusion WebUI（A1111 与 Forge，含 Forge Neo）的扩展，内置离线 SQLite 目录数据库：收录 39,006 个规范角色（背后 59,508 条来自 Danbooru/e621/AnimaDex 的源表示）与 19,800+ 画师风格。支持按名称、标签、作品别名搜索角色，可视化浏览画师风格并实时预览，一键将角色标签或画师签名发送到 txt2img 提示词。目录启动时经 SHA-256/SQLite 完整性校验，损坏时可从可信 GitHub 主机原子化重下；运行时副本额外占用约 94 MB 磁盘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置离线目录：39,006 角色与 19,800+ 画师风格（Danbooru/e621/AnimaDex 三源）
- 一键将角色标签与画师签名发送到 txt2img
- 目录启动时做 SHA-256、schema 与 SQLite 完整性校验，支持验证重下恢复
- 每源表示保留独立 prompt/trigger/rank，本地覆盖保存于 user_overrides_v2.json

## 适用场景

- 生图时查找不到角色准确 tag 的问题
- 浏览并试用不同画师风格改变生成画风
- 在 Danbooru/e621/Anima 之间切换同一角色的来源 prompt

## 场景标签

`提示工程` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L9: > **Extension for Stable Diffusion WebUI and Forge**
> L13: Your ultimate **character encyclopedia** and **artist style discovery** tool directly inside your Stable Diffusion 

## 星数曲线

```mermaid
xychart-beta
    title "eduardoabreu81/sd-character-finder 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-25"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-11-16 18 → 2026-11-25 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `95523facd7df` · [字段定义](../../DATASET.md)*
