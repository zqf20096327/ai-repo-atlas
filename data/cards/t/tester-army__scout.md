# tester-army/scout

⭐ 69 · TypeScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/tester-army/scout) · 组织维护

**面向 AI agent 的 OpenAPI 驱动 API 测试 CLI**

面向开发者的命令行 API 测试工具，设计给 AI agent 调用：解析 OpenAPI 规范或以无 spec 模式初始化，执行插桩请求、sweep、fuzz，生成 findings 与覆盖率报告，可作 CI 门禁。内置安全护栏：请求限定配置主机、默认阻断写方法、速率限制与请求预算、凭据从环境变量读取并脱敏输出。提供 agent init 安装配套技能到项目，支持请求链式取值、多身份认证配置与 JSON 输出。需 Node.js 22.12.0+，经 npx 运行。

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

- 解析 OpenAPI 规划 sweep/fuzz，输出 findings 与覆盖率报告及 CI 门禁
- 默认阻断写方法、主机锁定、速率限制、请求预算与凭据脱敏等护栏
- agent init 将版本匹配的技能安装到 .agents/skills/scout/
- 请求链式捕获变量与多认证 profile（--auth-profile）

## 适用场景

- 部署前让 AI agent 按真实用户流程测试 API
- 在 CI 中以覆盖率与确认 findings 作为门禁
- 测试角色与租户隔离（多认证 profile）

## 场景标签

 · 领域:开发者工具/API 测试

## 证据(README 行号)

> L8: Scout is an OpenAPI-driven API testing CLI built for AI agents. It parses your spec, executes instrumented requests,
> L182: |`scout agent init`|Install the bundled agent skill|

## 星数曲线

```mermaid
xychart-beta
    title "tester-army/scout 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 65 --> 70
    line [66, 69, 69]
```

2026-10-18 66 → 2026-10-29 69（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `19bb332aa484` · [字段定义](../../DATASET.md)*
