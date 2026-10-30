# mourner/claudefiles

⭐ 15 · JavaScript · MIT · 推送 2026-10-08 · [GitHub](https://github.com/mourner/claudefiles) · 个人维护

**Claude Code 效率工具集：状态栏、防浪费守卫与技能参考**

个人维护的 Claude Code 效率工具集，含三个组件：statusline 是 bash 状态栏脚本，显示模型、速率限额、成本、上下文 token 与缓存剩余时间；guard 是 PreToolUse 钩子，拦截明显浪费上下文或答错问题的 Read/Bash/WebFetch 调用（如超 64KB 文件读取、两点式 git diff），无法解析的调用一律放行；js-perf-notes 是 JavaScript/V8 性能优化技能参考，Claude 在优化任务时自动查阅。guard 与技能以插件安装，statusline 通过 settings.json 片段配置，依赖 bash 与 jq。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 状态栏显示速率限额、成本、上下文与缓存 TTL 及烧额速率警告
- PreToolUse 钩子拦截浪费上下文的工具调用，不确定即放行
- JavaScript/V8 性能优化技能参考，含按需查阅的瓶颈技术文件
- 支持插件安装或手动钩子/软链接两种方式

## 适用场景

- 在长会话中实时查看限额消耗与缓存剩余时间
- 阻止 AI 助手做出烧上下文的低效工具调用
- 优化 JS 热点代码时让 Claude 自动参考 V8 性能原则

## 场景标签

 · 领域:AI 开发者工具

## 证据(README 行号)

> L3: A few small Claude Code efficiency tools:
> L66: A single `hooks/guard.mjs` that runs before every `Read`, `Bash` and
> L11: The guard and skill ship as the installable `claudefiles` plugin (with more tooling to come);

## 星数曲线

```mermaid
xychart-beta
    title "mourner/claudefiles 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9982a7ea1275` · [字段定义](../../DATASET.md)*
