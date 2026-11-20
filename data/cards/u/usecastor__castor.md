# usecastor/castor

⭐ 14 · Rust · AGPL-3.0 · 推送 2026-11-19 · [GitHub](https://github.com/usecastor/castor) · [官网](https://usecastor.github.io) · 个人维护

**让云端编码代理把杂活交给本地 GPU 模型执行的 MCP 工具**

以 MCP 服务器形式接入 Claude Code、Cursor 等云端编码代理：规划仍由云端前沿模型完成，文件读取、grep、编辑、跑测试等机械性工作调度到用户本地 GPU 上的模型执行，仅将简短的验证结果回传云端，以减少按 token 计费的重复上下文。Rust 编写，内置零信任沙箱、token 预算调度器与流式守护；需自备本地 OpenAI 兼容推理引擎；AGPL-3.0 许可，网络部署的修改须开源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过一条 npx 命令向所有检测到的 MCP 客户端注册
- 支持 vLLM、llama.cpp、LM Studio、SGLang、Ollama 等任意 OpenAI 兼容引擎并自动探测
- 零信任沙箱：拦截路径逃逸、符号链接攻击与破坏性 shell 命令
- castor stats 输出本地处理 token 量、电费成本与工具调用成功率等统计

## 适用场景

- 在使用 Claude Code/Cursor 时把读文件、跑测试等任务转到本地 GPU 执行以降低云端 token 消耗
- air-gapped 环境下配合本地推理引擎运行代理工具链
- 统计与核算本地 LLM 处理的代理工作负载成本

## 场景标签

 · 领域:LLM 基础设施/开发工具

## 证据(README 行号)

> L11: Castor lets Claude Code, Antigravity, and Cursor hand the grunt work (reading, grepping, editing, running tests) to
> L78: |Claude Code · Google Antigravity · Cursor · Claude Desktop · any MCP client|vLLM · llama.cpp · LM Studio · SGLang 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `e96489043f7e` · [字段定义](../../DATASET.md)*
