# Mra1k3r0/nimji

⭐ 12 · TypeScript · MIT · 推送 2026-08-17 · [GitHub](https://github.com/Mra1k3r0/nimji) · [官网](https://deepwiki.com/Mra1k3r0/nimji) · 个人维护

**给开发者直连 Gemini 网页端点的 TS 客户端与终端 CLI**

以 Promise-first 的 TypeScript 库与同名 CLI 形式提供，直接调用 Gemini 网页版 `StreamGenerate` 接口：支持多轮会话持久化（session.json）、本地图片上传输入、图像生成模式（延长超时与重试）、keepalive 保活与 Cookie 自动轮换、可配置重试与流超时，并带终端 UI。凭据仅依赖浏览器 COOKIES 环境变量，AT_TOKEN/F_SID 经 bard-utils API 自动提取；支持 env/.env/config.jsonc 三层配置合并。

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

- Promise-first TS 库与 CLI 双形态，调用 Gemini web StreamGenerate
- 多轮会话持久化与 Cookie 自动轮换（/RotateCookies）
- 图片输入上传与图像生成管线，可本地保存或上传 ImgBB
- keepalive 保活、可配置重试与流超时

## 适用场景

- 在终端里以浏览器 Cookie 直接与 Gemini 多轮对话
- 让 Gemini 生成图像并保存到本地或托管到 ImgBB
- 在自己的 TypeScript 项目中以库形式调用 Gemini

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: **TypeScript client and CLI for Gemini web `StreamGenerate`**
> L27: nimji talks directly to the Gemini web `StreamGenerate` endpoint using your browser session. You only need **one th


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `af88addac618` · [字段定义](../../DATASET.md)*
