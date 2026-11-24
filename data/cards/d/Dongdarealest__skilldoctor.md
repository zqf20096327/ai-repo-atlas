# Dongdarealest/skilldoctor

⭐ 3 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/Dongdarealest/skilldoctor) · [官网](https://github.com/Dongdarealest/skilldoctor/blob/main/AUDIT.md) · 个人维护

**给开发者一键审计本机 AI 技能文件的安全 CLI**

零依赖的 Python 命令行工具，扫描机器上的 AI skill 指令文件，按有效性（frontmatter、命名规范）、安全风险（凭据引用、外发数据语句、隐藏 Unicode 等）、同名冲突与 token 成本四个维度给出 OK/WARN/FAIL 判定、百分制评分与修复建议；FAIL 技能可批量隔离到 quarantine 目录并可恢复。支持 --json 输出接入 CI，也可作为 GitHub Action 在每次 push 时自动审计。需要 Python 3.10+，无其他依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对已安装 skill 做有效性、安全、冲突、token 成本四类检查
- FAIL 技能可隔离到带清单的批次目录并用 --restore 恢复
- --json 与退出码 1 设计，可直接落入 CI/GitHub Action
- 通过审核的技能集合可获得动态徽章与注册表收录

## 适用场景

- 安装第三方 skill 前检查其中是否含危险指令
- 在 CI 中随每次 push 自动审计技能仓库
- 排查多个宿主目录下的同名/近似描述技能冲突

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L17: Skills are instruction files your AI loads and follows, often at the start of every conversation. Most people insta
> L38: Point it at any folder to audit just that folder, and add `--json` for machine readable output in scripts and CI. N


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `58c9561a932b` · [字段定义](../../DATASET.md)*
