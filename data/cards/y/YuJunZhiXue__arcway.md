# YuJunZhiXue/arcway

⭐ 15 · Go · 推送 2026-09-03 · [GitHub](https://github.com/YuJunZhiXue/arcway) · [官网](https://github.com/YuJunZhiXue/arcway) · 个人维护 · 中文 README

**自托管 LLM 网关：多上游聚合成 OpenAI/Claude/Gemini 兼容 API**

Go 后端加 Next.js 管理台的自托管 LLM 网关：把多家上游（OpenAI 兼容、Claude、Gemini、NVIDIA 自定义渠道及 Zen/Cline/FreeBuff 免费渠道）接到统一出口，提供模型路由（请求名映射上游模型、按序故障转移）、下游 API Key 创建与轮换、HTTP/SOCKS5/Xray 出口代理、用量管理与健康探针。管理台管理渠道、路由、账号与密钥，数据只落本机 data/ 目录。支持 Docker、Release 二进制与源码三种部署方式。声明仅供学习研究使用，不提供商业授权与稳定性保证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI/Claude/Gemini 三协议兼容出口（/v1/chat/completions、/v1/messages、generateContent）
- 模型路由：请求名映射上游模型，多候选按序故障转移
- 下游 API Key 可创建、复制、轮换、停用
- 渠道可绑定 HTTP/SOCKS5/Xray 出口换 IP

## 适用场景

- 把多个 LLM 上游账号聚合成一个统一 API 给客户端使用
- 给团队分发可控的下游 API Key 并管理用量
- 在 Cursor、Cline 等客户端填 Base URL 统一调用多渠道模型

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L14: 把多家上游接到一个 OpenAI / Claude / Gemini 兼容出口。核心后端是 **Go**，管理台是 **Next.js**（源码在 `frontend/`）。账号、密钥、渠道实例和数据库只写在本机 `data/`，
> L39: |OpenAI 兼容|`GET /v1/models`、`GET /v1/models/{id}`、`POST /v1/chat/completions`、`POST /v1/responses`、`GET /v1/respons
> L44: |模型路由|客户端只填你起的请求名，后台映射到真实上游模型，可按顺序故障转移|

## 星数曲线

```mermaid
xychart-beta
    title "YuJunZhiXue/arcway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9ac376723470` · [字段定义](../../DATASET.md)*
