# F0rger123/claude-business-god-mode

⭐ 3 · PowerShell · MIT · 推送 2026-11-15 · [GitHub](https://github.com/F0rger123/claude-business-god-mode) · 个人维护

**面向小型服务企业：用 Claude Code 运行 CRM/广告/SEO/视频四类工作**

由多个 Claude Code 插件组成的集合：以一份共享的业务档案（服务、价格、区域、品牌语气、预算）串联 CRM、Meta/Google 广告、SEO 审计和视频剪辑四个模块。安装后在 Claude Code 中用自然语言驱动，生成线索营销、网站评分、暂停状态的广告草稿和剪辑内容。核心机制是写入门控：花钱、发布、群发等动作需在对话中逐步确认，广告默认以 paused 状态创建，并有应急停止命令。CRM 为私有模板仓库，需有访问权限；代码以 PowerShell/Shell 脚本为主。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四模块共享一份业务档案，问答一次处处复用
- 写入门控：广告默认暂停创建，需逐步批准才执行
- /ads:emergency-stop 一条命令停止全部广告花费
- SEO 模块输出 Overall/SEO/AEO/GEO 评分与修复清单，附带 27 工具 MCP 服务器

## 适用场景

- 新开业服务商一周内搭起 CRM、网站评分与首批广告
- 代理机构为多个客户隔离运行业务档案
- 把手机拍摄素材剪成 reels/Shorts 并走客户审批

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L29: **Claude Business God Mode** is one front door to four tools that run the marketing and day-to-day of a small servi
> L84: > Nothing that spends money, goes public or messages customers happens until you say yes to that exact step. One co
> L56: /plugin marketplace add F0rger123/claude-business-god-mode

## 星数曲线

```mermaid
xychart-beta
    title "F0rger123/claude-business-god-mode 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-08 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `03d80e289ab1` · [字段定义](../../DATASET.md)*
