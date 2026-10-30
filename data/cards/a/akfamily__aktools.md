# akfamily/aktools

⭐ 1,503 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/akfamily/aktools) · [官网](https://aktools.akfamily.xyz/) · 个人维护 · 中文 README

**把 AKShare 千余财经数据接口封装为 HTTP API 与 MCP 服务**

基于 FastAPI 的服务：将 AKShare 的每个数据接口映射为 /api/public/<接口名> 端点，任何能发 HTTP 请求的语言（C++/Java/Go/Rust/R/MATLAB/Excel 等）可直接获取 JSON、CSV 或 Excel 数据；同时以 MCP 服务器形式接入 Claude、Cursor 等 AI 助手，提供 search_interfaces、describe_interface、get_data 三个工具供助手查找接口、填参取数。带 60 秒结果缓存、接口自查端点，提供 Dockerfile 与 Gunicorn 多进程部署方式，自身不带鉴权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AKShare 全部接口映射为 HTTP API，一行命令 python -m aktools 启动
- MCP 服务提供 3 个工具，供 Claude/Cursor 等 AI 助手自然语言查数
- 返回 JSON/CSV/Excel，支持任何可发 HTTP 请求的语言调用
- 结果缓存、接口搜索与参数自查、Docker 与 Gunicorn 部署

## 适用场景

- 非 Python 项目直接调用 AKShare 的中国财经数据接口
- 在 Claude/Cursor 中用自然语言查询股票行情与接口用法
- 团队局域网内部署统一财经数据服务

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L17: AKTools 把开源财经数据接口库 AKShare 的一千多个接口变成两种开箱即用的服务：
> L20: - **MCP 服务**：在 Claude、Cursor 等 AI 助手中直接用自然语言提问，助手会自己查找接口、填写参数并取回数据。


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9d7cf34a3a5a` · [字段定义](../../DATASET.md)*
