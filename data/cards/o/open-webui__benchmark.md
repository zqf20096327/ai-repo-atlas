# open-webui/benchmark

⭐ 27 · Python · MIT · 推送 2026-01-28 · [GitHub](https://github.com/open-webui/benchmark) · 组织维护

**Open WebUI 性能基准测试套件：测并发容量与响应时间**

针对 Open WebUI 的负载测试框架，通过 OpenAI 兼容 API、Playwright 驱动的真实 Chromium 浏览器 UI、Channels API 与 WebSocket 四类基准，测量并发用户容量、响应时间（P95）、吞吐与错误率；chat-ui 默认自动扩容模式逐步加压直至超出阈值以找最大可持续用户数。支持 5 种 CPU/内存计算档位的 Docker 容器资源约束，输出 JSON/CSV/文本报告，可通过 BaseBenchmark 类自定义场景。需 Python 3.11+ 与 Docker。

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

- 四类基准：chat-api、chat-ui（浏览器实测含渲染时间）、channels-api、channels-ws
- chat-ui 自动扩容模式自动找到 P95 阈值内的最大可持续并发用户数
- 5 种计算档位约束 Open WebUI 容器的 CPU/内存资源做对比测试
- owb CLI 运行，结果输出 JSON/CSV/摘要文本

## 适用场景

- 部署前测试 Open WebUI 实例能承载多少并发用户
- 对比不同服务器资源配置下的性能表现
- 验证 Channels 实时消息与 WebSocket 的并发上限

## 场景标签

 · 领域:LLM 应用性能评测

## 证据(README 行号)

> L3: A comprehensive benchmarking framework for testing Open WebUI performance under various load conditions.
> L116: Tests concurrent AI chat performance via the OpenAI-compatible API:

## 星数曲线

```mermaid
xychart-beta
    title "open-webui/benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5fa77fff037f` · [字段定义](../../DATASET.md)*
