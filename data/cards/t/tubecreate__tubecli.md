# tubecreate/tubecli

⭐ 174 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/tubecreate/tubecli) · [官网](https://tubecli.app) · 组织维护 · 中文 README

**自托管 AI agent 团队：用自然语言完成视频制作、建站部署与浏览器自动化**

TubeCLI 是基于 Python 3.10+/FastAPI 的自托管多 agent 系统：用户通过 CLI、Web 仪表盘、Telegram 或 Flow 画布用自然语言下达任务，由 agent 团队执行视频生成流水线（脚本→分镜→配图→配音→渲染→Drive/YouTube）、Cloudflare 建站九步部署、浏览器自动化（反检测配置文件、Keychain 凭据库）、字幕提取/翻译/克隆等操作。LLM 调用可全走本地 Ollama（无 API key）或 Gemini/OpenAI/Claude 等自带 key 的服务，常见流程走零 token 快速路径。不可逆操作需人工审批，任务带 JSONL 审计轨迹。MIT 许可，允许转售与白标。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- content_video 流水线：语料→脚本→分镜→图片→配音→Canvas Engine 渲染→Drive/YouTube，渲染可断点续传
- LLM 可全走本地 Ollama，无需 API key；常见流程用零 token 确定性意图匹配
- AI 创建的不可逆任务（部署/发布/删除）进入 pending_approval 等待人工审批
- 浏览器自动化：反检测配置文件、代理/指纹、Keychain 密码库、TOTP 2FA

## 适用场景

- 让 agent 把当天读过的文章自动做成带配音的 YouTube 视频
- 一句话让 agent 在自己的 Cloudflare 账号上部署一个真实网站
- 自动化登录、下载、发布等重复浏览器操作，必要时人工接管
- 把视频克隆成其他语言版本（新配音、同画面）

## 场景标签

`多智能体` `浏览器自动化` `视频生成` · 领域:Agent 开发

## 证据(README 行号)

> L22: **TubeCLI is a self-hosted, open-source AI agent team that executes real operational work end to end.** It is not a
> L95: **Models:** every LLM call runs on local Ollama — no API key, no per-token cost — or on Gemini, OpenAI, Claude, Dee

## 星数曲线

```mermaid
xychart-beta
    title "tubecreate/tubecli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 173 --> 175
    line [174, 174]
```

2026-10-18 174 → 2026-10-25 174（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `3e04db055748` · [字段定义](../../DATASET.md)*
