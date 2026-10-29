# duliangkuan/fengyun-publish

⭐ 25 · Python · MIT · 推送 2026-06-22 · [GitHub](https://github.com/duliangkuan/fengyun-publish) · 个人维护 · 中文 README

**单人微信公众号的 19 步 AI 写作发布流水线**

面向微信公众号运营者的端到端 AI 内容生产流水线，Python 脚本 + Claude Code skill 编排。覆盖选题、调研、写稿、三轨 critic 评审、排版、Seedream 配图、推送草稿箱共 19 步，以 gate.py 物理门控与 8 项 fake-pass 防伪字段拦截未真实执行的步骤，最后一步发布保留给人。依赖微信公众号 API、Anthropic Claude、火山引擎 Seedream、we-mp-rss/RSSHub Docker 容器等外部服务；KOL 语料与数据库不随仓库分发，需自行补齐。限制：仅 Windows + PowerShell 环境路径，需多项凭证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 19 个 BLOCKING Step + gate.py PreToolUse hook 物理拦截
- 三轨独立 critic 投票（数字分/灵魂判断/挂名意愿）+ 门控树
- 8 项 fake-pass 防伪字段与 critic-revise 3 轮自动出口
- 数据飞轮 + force_ship 学习回路（baseline 193→198）

## 适用场景

- 一个人运营 AI 赛道公众号，自动完成选题到草稿箱全流程
- 用多轨评审机制控制 AI 生成稿件质量
- 参考其 gate/防伪设计搭建自己的内容发布流水线

## 场景标签

`AI 写作` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L21: 一个**端到端的 AI 公众号写作发布流水线**,Python + Claude Code skill 编排。从「热点选题 → 深度调研 → 写稿 → 三轨评审 → 排版 → 封面 → 推草稿」一共 19 步,产出直接落到微信公众
> L129: |Anthropic Claude|所有 skill 底层|`ANTHROPIC_API_KEY`|

## 星数曲线

```mermaid
xychart-beta
    title "duliangkuan/fengyun-publish 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `dd5e4a911d63` · [字段定义](../../DATASET.md)*
