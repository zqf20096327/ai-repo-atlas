# KongFangXun/sofagent

⭐ 54 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/KongFangXun/sofagent) · [官网](https://www.npmjs.com/package/@sofagent/audit) · 个人维护 · 中文 README

**给 AI coding agent 加治理层：按冻结规则审计每次变更**

开源 FDE Harness 治理层，嵌在 Agent（DSH/OpenClaw/WorkBuddy/Claude Code 等）与模型层之间：进场阶段把业务判断写成文件（工作流、本体、AI 节点的 merge_criteria/approver/trigger），离场阶段按文件在 commit 时自动审计。提供 28 条审计规则（密钥泄漏、越界编辑、注入防御、权限红线）、HAML 防篡改审计链（原文如此：HMAC）、自动快照回滚、104 个 MCP tool 与 12 插件。以 npm 伞包与 install.sh 双通道安装；限制：默认非 fail-closed、`--no-verify` 可跳过前两层防线、判定层 S1M 尚未交付（排期 v1.6.0–v1.9.0）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 28 条审计规则覆盖密钥/越界/注入/权限/后门，commit 时硬拦截
- 审计历史落 HMAC 链，`--verify-chain` 离线复算，支持快照一键回滚
- 104 个 MCP tool + 12 插件，五种挂载形态（插件/Skill/MCP/CLI/Dashboard）
- npx 零配置审计：任意 git 仓库单次引擎审计约 1.1 秒

## 适用场景

- 给已有的 coding agent 加提交级审计，拦截密钥泄漏与越界编辑
- 一人公司或小企业按文件化管理 AI 节点的岗位职责与做好标准
- 审计出事后通过快照回滚与 HMAC 证据链追溯 Agent 变更

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L29: **开源 FDE Harness 层**（Harness = 「缰绳」，套住 Agent 的治理层；FDE = Forward Deployed Engineer 前线部署工程师，详见〈什么是 FDE Harness〉）——嵌在成
> L30: sofagent 不造 Agent——交付的是让任何 Agent 被管住的那一层（管住强度按宿主分档：DSH/OpenClaw 硬注入可拦截，其余档位为建议性注入 + git hook 审计兜底——见〈多平台挂载〉档位表）。
> L100: - 🔧 **工具与能力面：104 个 MCP tool + 证据分档**——28 条规则中 22 条基于 git diff（本地生效、零 token）、4 条 hybrid（diff + Agent 日志）、1 条 filesy

## 星数曲线

```mermaid
xychart-beta
    title "KongFangXun/sofagent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-28 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `abde76b534d2` · [字段定义](../../DATASET.md)*
