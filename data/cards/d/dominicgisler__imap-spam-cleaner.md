# dominicgisler/imap-spam-cleaner

⭐ 19 · Go · GPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/dominicgisler/imap-spam-cleaner) · 个人维护

**自托管工具：用 AI 判分自动清理 IMAP 收件箱垃圾邮件**

从配置的 IMAP 邮箱加载邮件，调用所配置的检查提供方（OpenAI、Ollama、Gemini、TypeSafe、SpamAssassin 或 rspamd）对邮件内容进行判定，依据垃圾邮件分数将邮件移入垃圾邮件文件夹，保持收件箱整洁。以 Docker 镜像形式提供，通过挂载 config.yml 运行，属自托管应用。详细配置方式见其文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取 IMAP 收件箱邮件并按垃圾分数自动移动到垃圾文件夹
- 支持多种判定提供方：OpenAI、Ollama、Gemini、TypeSafe、SpamAssassin、rspamd
- 以 Docker 镜像分发，配置文件挂载即可运行

## 适用场景

- 自托管清理自己 IMAP 邮箱中的垃圾邮件
- 用本地 Ollama 模型判定垃圾邮件，不依赖外部 API

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L19: This application loads mails from configured IMAP inboxes and checks their contents using the defined provider
> L20: (OpenAI, Ollama, Gemini, TypeSafe, SpamAssassin or rspamd).

## 星数曲线

```mermaid
xychart-beta
    title "dominicgisler/imap-spam-cleaner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f01b153a91d1` · [字段定义](../../DATASET.md)*
