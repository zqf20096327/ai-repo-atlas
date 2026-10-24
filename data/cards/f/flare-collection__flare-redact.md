# flare-collection/flare-redact

⭐ 52 · TypeScript · MIT · 推送 2026-08-09 · [GitHub](https://github.com/flare-collection/flare-redact) · [官网](https://flare-collection.github.io/flare-redact/) · 组织维护

**零依赖 TypeScript 密钥与 PII 脱敏库，覆盖日志与 LLM 提示词**

通过读取文本内容（而非仅字段名）检测并掩码密钥、令牌、卡号、邮箱等敏感信息，支持 24 种语言、82 个检测器。提供 LLM 客户端包装（OpenAI/Anthropic）：提示词中敏感值替换为不透明占位符，回复时还原，模型不接触原始值。另含通用中间件（包裹任意 SDK/函数边界）、Docker 反向代理网关（无需改代码）与 GitHub Actions 密钥扫描；Python/Go/Rust 引擎执行同一 FRS-1 检测器规范并共享一致性测试集。运行时零依赖，Node 20+/浏览器/edge 可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内容级检测：从文本内容识别 AWS 密钥、JWT、卡号等并掩码
- LLM 客户端包装：提示词脱敏、回复还原，模型不接触原始值
- 四语言引擎（JS/Python/Go/Rust）执行同一 FRS-1 规范，同一策略输出一致
- Docker sidecar 网关：改 base URL 即完成集成，支持流式还原与 Prometheus 指标

## 适用场景

- 在日志进入聚合器/错误追踪器之前掩码其中的密钥与 PII
- 防止用户数据（邮箱、卡号、API key）随提示词离开系统
- 为异构技术栈（Python/PHP/Node 共用同一供应商）提供免改码的统一脱敏入口
- 在 Pull Request 中扫描源码与配置文件里的密钥与 PII

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L42: > **The same problem now has a new address: your LLM calls.** Wrap your OpenAI or
> L271: ## Redact prompts before they reach an LLM
> L286: ```

## 星数曲线

```mermaid
xychart-beta
    title "flare-collection/flare-redact 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-24 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `807f180e0d65` · [字段定义](../../DATASET.md)*
