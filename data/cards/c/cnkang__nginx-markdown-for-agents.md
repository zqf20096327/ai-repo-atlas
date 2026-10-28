# cnkang/nginx-markdown-for-agents

⭐ 25 · Python · BSD-2-Clause · 推送 2026-10-27 · [GitHub](https://github.com/cnkang/nginx-markdown-for-agents) · 个人维护 · 中文 README

**NGINX 模块：通过 Accept 协商向 AI agent 返回 Markdown**

自托管的 NGINX 动态模块，在边缘将已服务的 HTML 页面转换为 Markdown：客户端发送 Accept: text/markdown 即收到 Markdown，浏览器仍收到原 HTML，也可通过 User-Agent 匹配对指定 bot 强制返回。转换由 Rust 转换器经 C/Rust FFI 完成。提供全缓冲与有界流式两种转换模式，处理 gzip/deflate/Brotli 压缩，支持 ETag 条件请求、链接净化、错误策略与 Prometheus 指标。0.9.2 为破坏性版本，配置冻结为 20 条指令；动态模块必须与加载它的 NGINX 精确版本匹配。面向自建站点运营者与为 AI 爬虫/agent 准备内容的团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Accept: text/markdown 内容协商，浏览器不受影响
- User-Agent 匹配可对指定 bot 强制返回 Markdown
- gzip/deflate/Brotli 压缩处理与有界流式转换
- deb/rpm 包、Homebrew、Docker 镜像与源码构建多渠道分发

## 适用场景

- 让自家站点在不改应用代码的情况下向 AI agent 提供 Markdown
- 对 ClaudeBot 等 AI 爬虫定向返回精简 Markdown
- 减少 agent 抓取页面时的 token 消耗

## 场景标签

 · 领域:Web 基础设施/AI agent 内容服务

## 证据(README 行号)

> L14: NGINX Markdown for Agents adds a machine-friendly Markdown representation to
> L15: HTML pages that you already serve. Clients that send `Accept: text/markdown`
> L104: Many AI crawlers send browser-style `Accept` headers. Use NGINX `map` to select

## 星数曲线

```mermaid
xychart-beta
    title "cnkang/nginx-markdown-for-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c08d0d49fc92` · [字段定义](../../DATASET.md)*
