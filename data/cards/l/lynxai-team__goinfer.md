# lynxai-team/goinfer

⭐ 14 · Go · MIT · 推送 2026-10-11 · [GitHub](https://github.com/lynxai-team/goinfer) · [官网](https://synw.github.io/goinfer/) · 组织维护

**本地 LLM 推理代理：在远程 GPU 机器上切换 GGUF 模型并经 API 暴露**

基于 llama.cpp 与 llama-swap 的 Go 编写推理代理：在 GPU 机器上加载多个 *.gguf 模型、运行时切换并修改推理参数，通过 OpenAI 兼容的 /v1/ 与 llama.cpp 兼容的 /completions HTTP API 暴露服务，带 API key 鉴权与 CORS 控制，可远程上传/删除模型、git pull 并重编译 llama.cpp。面向希望从任意设备安全连接家庭/办公室 GPU 的本地 LLM 用户与 DevOps 场景。注意：README 中客户端/服务端反向连接模式标注为尚未实现（L13、L250），当前可用形态为单机代理；项目 2025 年 8 月起改用 llama-swap 管理进程，不再支持 Ollama/KoboldCpp。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 加载多个 *.gguf 模型并支持运行时切换
- OpenAI 兼容 /v1/ 与 llama.cpp 兼容 /completions API、流式响应
- API key 鉴权、CORS 控制、远程上传/删除 GGUF 与重载配置
- 提供 clone-pull-build-run.sh 脚本自动克隆/编译 llama.cpp 并生成配置

## 适用场景

- 把家用 GPU 机器上的本地模型通过 HTTP API 提供给其他设备调用
- 在 Cline/RooCode 等工具中接入本地 GGUF 模型推理
- 远程管理 GPU 机器上的模型文件与 llama.cpp 依赖更新

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: **Inference proxy** – swap between multiple `*.gguf` models on remote machines and expose them through HTTPS-API wit
> L7: Built on top of llama.cpp and llama-swap, Goinfer is designed to be DevOps-friendly, easily deployable/monitored on 
> L30: **API** | OpenAI-compatible HTTP API `/v1/`, LLama.cpp-compatible `/completions` API, streaming responses

## 星数曲线

```mermaid
xychart-beta
    title "lynxai-team/goinfer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5d1714db284b` · [字段定义](../../DATASET.md)*
