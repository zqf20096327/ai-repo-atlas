# malvads/mojo

⭐ 16 · C++ · MIT · 推送 2026-06-07 · [GitHub](https://github.com/malvads/mojo) · 个人维护

**C++20 多线程网站爬虫，把整站转为 LLM 可用的 Markdown**

面向 LLM/AI 数据摄取的命令行爬虫：用 C++20 协程与线程池异步抓取整站，将 HTML 转为结构化 Markdown，用于构建知识库与 RAG 管线。支持 SOCKS4/SOCKS5/HTTP 代理轮换与死代理自动剔除；--render 模式通过无头 Chromium 渲染 JS 动态内容，并用内置反向代理网关实现按请求切换 IP。遵循 robots.txt。提供 Linux/macOS/Windows 预编译二进制，也可从源码用 CMake 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- C++20 协程 + 线程池架构的异步高并发抓取
- HTML 自动转为面向向量数据库/LLM 的 Markdown
- SOCKS4/SOCKS5/HTTP 代理轮换、优先级选择与死代理自动剔除
- --render 模式用无头 Chromium 渲染动态内容，反向代理网关按请求切换 IP

## 适用场景

- 把文档站或博客整站抓取为 Markdown 供 RAG 知识库使用
- 为 LLM 训练准备清洗后的文本数据集
- 抓取需要 JS 渲染的 SPA 站点内容

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L19: Mojo is a high-performance, multithreaded web crawler tailored for creating high-quality datasets for Large Languag
> L57: - **RAG-Ready Data Ingestion**: Automatically transforms noisy HTML into clean, token-efficient Markdown. Perfect f

## 星数曲线

```mermaid
xychart-beta
    title "malvads/mojo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a2c325ae6570` · [字段定义](../../DATASET.md)*
