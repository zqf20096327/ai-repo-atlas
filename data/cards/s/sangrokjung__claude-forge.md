# sangrokjung/claude-forge

⭐ — · [GitHub]() · 个人维护 · 中文 README

**Claude Code 的配置增强套件：一次安装获得 16 agents、35 命令、33 技能与 22 hooks**

面向 Claude Code 用户的“装备包”（类比 oh-my-zsh 之于 zsh）：一次安装注入 16 个专家 agent、35 个斜杠命令、33 个技能、22 个安全 hooks、14 个规则文件与 4 个 MCP 连接（Playwright、context7、jina-reader、Chrome DevTools）。v4.0 引入对抗式验证环：独立第二 agent 不看第一 agent 的推理过程，输出 APPROVE/REQUEST_CHANGES 判定。提供 Claude Code 插件与 install.sh 两条安装路径，Windows 有 PowerShell 脚本；插件方式不含 agents/hooks/rules。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 个专家 agent（planner、adversarial-reviewer、systematic-debugger 等）+ 35 个斜杠命令
- 对抗式验证环：maker≠checker，独立 agent 复核每个行为变更
- 22 个后台 hooks：密钥泄漏拦截、危险命令阻断、API 错误自动恢复、doom-loop 防护
- 4 个 MCP 外部工具连接（Playwright 浏览器自动化、context7、jina-reader、Chrome DevTools）

## 适用场景

- 给 Claude Code 补齐规划、TDD、代码审查、安全扫描等预设工作流
- 在无人值守场景靠 hooks 拦截危险命令与密钥泄漏
- 用对抗式验证环复核 AI 生成的行为变更

## 场景标签

 · 领域:AI 编码工具/开发者配置

## 证据(README 行号)

> L41: Claude Forge is the **equipment pack** for that assistant. One install gives it:
> L50: > **The oh-my-zsh analogy:** oh-my-zsh is a free add-on that turns a plain terminal into a colorful, plugin-packed 
> L122: |**Agents** (specialist colleagues)|16|Each one is an AI focused on a single job — planner, architect, security ch

## 星数曲线

```mermaid
xychart-beta
    title "sangrokjung/claude-forge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 857 --> 861
    line [858, 860, 860]
```

2026-10-18 858 → 2026-10-21 860（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `d38b575490f9` · [字段定义](../../DATASET.md)*
