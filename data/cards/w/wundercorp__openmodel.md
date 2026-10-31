# wundercorp/openmodel

⭐ 18 · TypeScript · Apache-2.0 · 推送 2026-08-14 · [GitHub](https://github.com/wundercorp/openmodel) · [官网](https://openmodel.sh) · 组织维护

**本地/云端模型网关运行时，含 token 遥测与 GPU 算力市场**

以 npm 包 @wundercorp/openmodel 分发的网关式本地模型运行时：om pull 支持 Hugging Face GGUF、直链 URL 与 Ollama 模型引用；om run 驱动 llama.cpp 与 Ollama 运行时；om serve 提供 OpenAI 兼容与 Ollama 兼容本地端点及用量指标。另含 GPU 算力市场（worker 注册、心跳、计量、结算）、Box 隔离 Agent VM、OIDC 登录与 AWS/Cloudflare 部署方案。限制：只能运行已安装运行时支持的格式。面向开发者，许可证 Apache-2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- om pull/run/serve 覆盖 GGUF、Ollama 引用与 OpenAI 兼容本地端点
- 本地指标：请求计数、token 估算、延迟、吞吐与按模型用量
- GPU 提供方市场：注册、心跳、预留、计量与结算流程
- 网关插件体系，运行时与网关解耦

## 适用场景

- 本地统一拉取并运行 GGUF / Ollama 模型，暴露 OpenAI 兼容 API
- 在仪表盘中查看本地推理的 token 用量与成本对比
- 将自有 GPU 机器注册为算力提供方并结算收益

## 场景标签

`模型网关` `推理引擎` · 领域:Agent 开发

## 证据(README 行号)

> L3: OpenModel is a gateway-first local model runtime distributed as `@wundercorp/openmodel`, with a baseui.sh-powered da
> L14: - `om run` for llama.cpp and Ollama runtimes
> L15: - `om serve` with OpenAI-compatible and Ollama-compatible local endpoints

## 星数曲线

```mermaid
xychart-beta
    title "wundercorp/openmodel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4aa30b6b3dfd` · [字段定义](../../DATASET.md)*
