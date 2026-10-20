# Ebony-Vinyl/dsh-our-free-model

⭐ 24,470 · JavaScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/Ebony-Vinyl/dsh-our-free-model) · 个人维护 · 中文 README

**dsh 插件：免登录免 Key 使用免费前沿模型清单**

挂载在 dsh 宿主上的插件，安装后无需账号与 API Key 即可在模型选择器中使用上游免费车道提供的模型（如 DeepSeek V4.1 Flash、Kimi K3）。模型清单每次刷新向上游重新拉取，不存静态快照；选择器按本机网络出口实测剔除网关拒绝路由的模型。附带 OpenAI 与 Anthropic 兼容的本地转发端口、用量看板、思考强度下发、聚合渠道（内置 75 家提供商注册表）与降级链路由。通过仓库 Release 包或本地源码目录安装，README 明确警告 npm 上的同名包非本仓库发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 18,11 位贡献者
- 涨星:近 1 天 **+2,787**(自 20261016 起算)
- 平台:— · 协议:OPENAI-API / OLLAMA

## 能力要点

- 免登录、免注册、免 API Key 使用免费模型，清单跟随上游刷新
- 本地网关支持 Chat Completions、Responses 与 Anthropic Messages 端点
- 聚合渠道注册表内置 75 家提供商（NVIDIA NIM、OpenRouter、Groq、Ollama 等）
- 应用内一键升级：SHA-256 校验、原子替换、失败回滚、热重载

## 适用场景

- 在 dsh 里不注册账号直接调用免费前沿模型
- 把免费模型经本地端口暴露给本机其它工具调用
- 把多个渠道模型串成降级链做轮换与回退

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L18: > 你只需在 dsh 里装上这个插件，无需登录、注册、填 API Key 或任何其它操作，
> L48: - **聚合渠道，自带 Key**——设置页新增一页，把第三方端点接进同一条模型清单：注册表内置 75 家提供商（NVIDIA NIM、OpenRouter、Groq、Cerebras、SambaNova、Gemini、DeepS
> L96: ## 安装

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `a9d187412217` · [字段定义](../../DATASET.md)*
