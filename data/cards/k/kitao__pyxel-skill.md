# kitao/pyxel-skill

⭐ 15 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/kitao/pyxel-skill) · [官网](https://github.com/kitao/pyxel-mcp) · 个人维护

**指导 agent 开发与验证 Pyxel 复古游戏的 Claude 技能插件**

面向 Claude Code 及其他 agent 的 Agent Skill：引导 Pyxel 游戏的实现与验证，配套捆绑 pyxel-mcp MCP 服务器提供观察工具。可作为 Claude Code 插件（claude plugin 命令）安装，自动注册 pyxel MCP 服务器；也支持 skills CLI（npx skills add）与手动 git clone。版本 1.4.3 要求 pyxel-mcp>=1.3.1、Pyxel>=2.9.6、Python>=3.11；对 Codex 等客户端给出 MCP 手动注册说明。MIT 许可。

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

- 引导 Pyxel 游戏实现与验证的 Agent Skill
- 捆绑 pyxel-mcp MCP 服务器并随插件自动注册
- 支持 Claude 插件安装、npx skills CLI 与手动 clone 三种途径
- 内置 pytest 测试与技能内容校验流程

## 适用场景

- 让 Claude Code 按 skill 引导开发 Pyxel 复古游戏
- 为其他 agent 客户端注册 Pyxel MCP 观察工具
- 验证已生成的 Pyxel 游戏实现

## 场景标签

`编码 Agent` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: An Agent Skill for building and verifying Pyxel games. It guides implementation and verification for the requested g
> L22: The plugin registers the `pyxel` MCP server as `uvx --from 'pyxel-mcp>=1.3.1' pyxel-mcp`, so do not add the server 

## 星数曲线

```mermaid
xychart-beta
    title "kitao/pyxel-skill 星数(近 3 点)"
    x-axis ["2026-10-22", "2026-10-26", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-22 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `f24d147bfc72` · [字段定义](../../DATASET.md)*
