# TurtleByte-IN/mailrules

⭐ 4 · Go · AGPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/TurtleByte-IN/mailrules) · [官网](https://mailrules.app/?utm_source=github&utm_medium=repo-about) · 组织维护

**自托管邮件规则分类守护进程：用自然语言规则整理 IMAP 收件**

以守护进程形式通过 IMAP 实时处理新到邮件，规则可用纯英文书写或以结构化条件定义；支持任意以密码/应用密码登录的 IMAP 邮箱（iCloud、Gmail、Fastmail、Yahoo、Zoho、经 Bridge 的 Proton Mail、自有服务器），用户可选择决定分类的模型并配置密钥。默认仅监听本机、dry-run 开启，先记录动作不改邮箱。以单二进制（内置 Web UI）、Docker 镜像或 Homebrew cask 分发；Outlook.com 与 Microsoft 365 登录未包含。仅结构化条件组成的规则无需模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯英文或结构化条件两种规则写法，实时 IMAP 分类
- 默认 dry-run 模式，切换前不修改邮箱
- 单二进制内置 Web UI，支持 Linux/macOS amd64 与 arm64
- 通过公共 Go 包 ext 可扩展模块（托管版含从邮件建议规则的模块）

## 适用场景

- 自托管场景下按自然语言规则自动归档新邮件
- 将订阅邮件分入 Jobs/Reading/Trash 等文件夹
- 在 dry-run 下先观察分类结果再实际生效

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: MailRules is a small daemon that sorts incoming email over IMAP, in real time, using rules you write in plain Englis
> L66: 2. Choose the decision model and give it a key, or skip that: rules made only of conditions need no model.

## 星数曲线

```mermaid
xychart-beta
    title "TurtleByte-IN/mailrules 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-20", "2026-11-22"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-08 3 → 2026-11-22 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `761d4f494203` · [字段定义](../../DATASET.md)*
