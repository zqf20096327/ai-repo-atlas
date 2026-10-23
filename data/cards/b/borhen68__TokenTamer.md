# borhen68/TokenTamer

⭐ 128 · Python · MIT · 推送 2026-06-15 · [GitHub](https://github.com/borhen68/TokenTamer) · 个人维护

**给 AI 编码代理省 token 的代理：实时压缩代码上下文**

介于 AI 编码代理与 LLM API 之间的中间件代理：拦截请求载荷，用 AST/括号平衡启发式把非活跃文件压缩为结构骨架（保留签名、导入、类结构），并对 tool_result 中的旧文件读取做骨架化、保留每文件最近一次读取。另对 Anthropic 注入 cache_control 断点实现前缀缓存命中。支持 OpenAI 与 Anthropic 端点，适配 Aider/Cursor/Claude Code/Codex CLI 等客户端。自述 alpha 阶段，节省数据来自合成载荷单元测试而非真实生产基准；硬编码端点的客户端需 HTTPS 拦截与证书信任。

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

- AST 压缩：剥离函数体、保留签名/导入/类结构，支持 Python 及 6 类语言（启发式）
- tool 感知压缩：骨架化旧 tool_result 文件读取，保留最新读取
- 向 Anthropic 请求注入 cache_control 断点，保持前缀字节一致以提高缓存命中
- 终端实时显示 token 与费用节省，SSE 流式透传

## 适用场景

- 长会话 Claude Code/Aider 编码代理降低 API 输入成本
- 通过改 base URL 无侵入接入现有编码代理
- 观测各会话的 token 节省情况

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: TokenTamer is a middleware proxy that sits between an AI coding agent and the LLM API. It intercepts raw payloads, p
> L289: |Provider|Endpoint|Status|

## 星数曲线

```mermaid
xychart-beta
    title "borhen68/TokenTamer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 127 --> 129
    line [128, 128]
```

2026-10-18 128 → 2026-10-23 128（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `479e421125c1` · [字段定义](../../DATASET.md)*
