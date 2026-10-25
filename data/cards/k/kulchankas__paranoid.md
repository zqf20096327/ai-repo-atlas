# kulchankas/paranoid

⭐ 48 · Python · MIT · 推送 2026-09-27 · [GitHub](https://github.com/kulchankas/paranoid) · 个人维护

**AI 编程 agent 的安全技能：对本地运行的应用做渗透测试并修复**

以 Markdown 技能形式交付的 agent skill，供 Claude Code、Codex、Cursor 等编程 agent 使用。/hack-me 命令对本地运行的应用执行 find→prove→patch→re-verify 循环：映射应用路由与认证结构，针对风险类别构造请求，以真实 HTTP 请求证明每个漏洞存在，打最小化补丁后重放漏洞验证修复，并在未探测路径上扫描同类问题。识别 12 种技术栈（Next.js、FastAPI、Django 等）的路由与认证位置。限制为仅 localhost、授权目标、非破坏性验证；附可复现的基准测试框架（22/24 类已评分）。

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

- 以真实 HTTP 请求证明漏洞存在，不以推测判定
- patch 后重放原漏洞请求验证修复，并扫描未探测路径的同类问题
- 覆盖 12 种技术栈的路由与认证位置识别
- 附可复现基准测试框架，CI 校验评分有效性

## 适用场景

- 开发中的应用上线前让 agent 自动渗透测试并修复漏洞
- 用 /hack-me 验证自己写的代码是否真正挡住攻击
- 随编码过程加载配套安全指南与 pre-commit 检查

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L11: An agent skill that pentests the app you're building. `/hack-me` attacks your own
> L41: **Codex, Cursor, or any agent that reads skills:**
> L50: No dependencies, no network calls, no telemetry — it's Markdown your agent reads.

## 星数曲线

```mermaid
xychart-beta
    title "kulchankas/paranoid 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-25 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8955491384db` · [字段定义](../../DATASET.md)*
