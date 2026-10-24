# chigwell/skilldock.io

⭐ 87 · Python · Apache-2.0 · 推送 2026-07-05 · [GitHub](https://github.com/chigwell/skilldock.io) · [官网](https://skilldock.io/) · 组织维护

**面向 AI Skill 注册表 SkillDock 的 Python SDK 与 CLI 客户端**

skilldock 是 SkillDock.io API 的 OpenAPI 驱动 Python 客户端与命令行工具，用于发现、安装、发布基于 AgentSkills 规范的版本化 AI Skill。运行时加载 OpenAPI 规范，暴露可调用任意 operationId 的 SkilldockClient 与 CLI。支持浏览器 OAuth 登录与个人 API token 认证、递归依赖解析的本地安装、按 SKILL.md frontmatter 读取标签的 zip 上传发布、发布版本不可变、按版本存储描述，以及含 TON 支付（Stripe 暂不可用）的买卖流程。面向需要程序化或命令行操作 Skill 注册表的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 运行时加载 OpenAPI 规范，可调用任意 operationId 的客户端与 CLI
- skill install 支持递归依赖解析，公开 Skill 无需认证即可安装
- 发布版本不可变，描述按版本（description_md）存储与回退
- 支持浏览器 OAuth 登录、个人 API token 与 TON 支付买卖流程

## 适用场景

- 在终端搜索、安装、卸载 SkillDock 注册表中的 AI Skill
- 将自己的 Skill 打包为版本化发布并上传到注册表
- CI 中通过个人 API token 调用 SkillDock API 管理技能

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L12: `skilldock` is an OpenAPI-driven Python client (and a CLI) for the SkillDock API.
> L106: Install a skill locally (default destination is `./skills`, with recursive dependency resolution):
> L140: This packages the folder into a zip and uploads it as multipart form field `file`.

## 星数曲线

```mermaid
xychart-beta
    title "chigwell/skilldock.io 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 86 --> 88
    line [87, 87]
```

2026-10-18 87 → 2026-10-24 87（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e9254533ddd4` · [字段定义](../../DATASET.md)*
