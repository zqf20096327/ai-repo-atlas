# 0-to-1-Labs/claude-code-prompt-optimizer

⭐ 48 · TypeScript · MIT · 推送 2026-09-30 · [GitHub](https://github.com/0-to-1-Labs/claude-code-prompt-optimizer) · 组织维护

**Claude Code 钩子：把简短提示词扩写为结构化指令**

以 Claude Code 插件/hook 形式提供的提示词改写工具：在提示词前加 <optimize> 标签，hook 拦截后经 Claude Agent SDK 将请求发送给会话当前模型做单轮无工具改写，产出含实现步骤、错误处理、测试要求与边界情况的结构化版本，作为 additionalContext 返回。无标签提示在 bash 层短路，不加载 Node。支持 OAuth/API key/存储凭据三种认证、模型别名与回退链、超时预算与 fail-open；超长提示（默认 12,000 字符）直接放行。需 Claude Code CLI 与 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- <optimize> 标签触发的单轮无工具提示词改写，复用会话当前模型
- 无标签提示在 bash 层短路，正常路径零延迟
- 回退模型链、按模型家族的时间预算与 fail-open 机制
- 元数据日志（模型/耗时/成本）不含提示词文本与凭据

## 适用场景

- 把一句话需求扩写成含步骤与测试要求的结构化提示
- 在 Claude Code 中自动完成提示词工程
- 切换会话模型后仍保持改写模型与执行模型一致

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L13: When you tag a prompt with `<optimize>`, this hook intercepts it and sends it to the same model your session is run

## 星数曲线

```mermaid
xychart-beta
    title "0-to-1-Labs/claude-code-prompt-optimizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-30 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3c22384564d6` · [字段定义](../../DATASET.md)*
