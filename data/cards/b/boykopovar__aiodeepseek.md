# boykopovar/aiodeepseek

⭐ 15 · Python · MIT · 推送 2026-05-22 · [GitHub](https://github.com/boykopovar/aiodeepseek) · 个人维护

**DeepSeek 私有 API 的异步 Python 客户端库**

面向 Python 开发者的异步客户端库，通过逆向工程的 DeepSeek 私有 API 提供访问：支持邮箱/密码与 token 两种认证、流式输出、多轮对话、图片上传与新账号注册，并区分 DEFAULT/EXPERT/VISION 三种模型类型。请求前自动求解服务端下发的 PoW 挑战（典型难度 14.4 万次迭代），计算由 C++/AVX2 扩展实现；也可下载预编译 release。要求 Python 3.9+ 与 aiohttp>=3.9，构建扩展需支持 AVX2 的 C++17 编译器。提供俄语文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 异步客户端，支持流式输出、多轮对话与图片上传
- 自动求解服务端 PoW 挑战（C++/AVX2 扩展，典型 144,000 次迭代）
- 支持邮箱/密码与 token 认证及新账号注册
- 三种模型类型：DEFAULT/EXPERT（深度推理）/VISION（机器视觉）

## 适用场景

- 在 Python 异步应用中接入 DeepSeek 对话与流式输出
- 上传图片调用 DeepSeek 视觉模型
- 程序化管理 DeepSeek 账号注册与 token 认证

## 场景标签

 · 领域:LLM API 客户端

## 证据(README 行号)

> L8: A high-performance async Python client for the private DeepSeek API. Supports streaming, image uploads, multi-turn c
> L15: pip install aiodeepseek

## 星数曲线

```mermaid
xychart-beta
    title "boykopovar/aiodeepseek 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0b93113ff1d2` · [字段定义](../../DATASET.md)*
