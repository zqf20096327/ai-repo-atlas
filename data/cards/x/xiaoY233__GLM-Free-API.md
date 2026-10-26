# xiaoY233/GLM-Free-API

⭐ 64 · TypeScript · GPL-3.0 · 推送 2026-02-26 · [GitHub](https://github.com/xiaoY233/GLM-Free-API) · [官网](https://open.bigmodel.cn/) · 个人维护 · 中文 README

**智谱清言逆向 API 服务：兼容 OpenAI/Gemini/Claude 接口格式**

将智谱清言网页端封装为 API 服务的项目，由 LLM-Red-Team/glm-free-api 修改而来，称已移除原项目中的恶意代码。提供与 OpenAI、Google Gemini、Anthropic Claude 兼容的三种接口格式，支持流式输出、多轮对话、智能体对话、沉思模型、视频生成、AI 绘图、联网搜索等。通过浏览器 Cookie 提取 refresh_token 鉴权，支持多账号 token 拼接。以 Docker 镜像部署。README 声明项目已停止更新、仅供自用研究，逆向 API 不稳定且有封禁风险。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI/Gemini/Claude 三种兼容接口（含 gemini-cli、Claude-code 适配器）
- 多账号 refresh_token 拼接与自动挑选
- 支持流式输出、多轮对话、智能体对话、沉思/Zero 推理模型
- Docker 一条命令部署，8000 端口开放即用

## 适用场景

- 用 OpenAI 兼容客户端调用智谱清言对话能力
- 在 gemini-cli 或 Claude-code 中接入该 API
- 配合 Dify 等线上服务搭建对话工作流

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: 支持GLM-4-Plus高速流式输出、支持多轮对话、支持智能体对话、支持沉思模型、支持Zero思考推理模型、支持视频生成、支持AI绘图、支持联网搜索、支持长文档解读、支持图像解析，零配置部署，多路token支持，自动清理会话痕迹。
> L163: 1. 与OpenAI兼容的 `/v1/chat/completions` 接口
> L165: 3. 与Anthropic Claude兼容的 `/v1/messages` 接口

## 星数曲线

```mermaid
xychart-beta
    title "xiaoY233/GLM-Free-API 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 62 --> 65
    line [63, 64, 64]
```

2026-10-18 63 → 2026-10-26 64（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4ff9635d7c3a` · [字段定义](../../DATASET.md)*
