# iamgmujtaba/llama3.2-webUI

⭐ 35 · PHP · MIT · 推送 2026-10-05 · [GitHub](https://github.com/iamgmujtaba/llama3.2-webUI) · [官网](https://gmujtaba.com/) · 个人维护

**面向 Ollama 的 Llama 3.2 多模态网页对话界面**

基于本地 Ollama 平台的 Web UI 项目：通过 llama3.2 模型向用户提供文本问答、代码高亮输出与复制等交互功能，宣称支持图像输入（README 标注 Coming soon）。安装方式为克隆仓库后运行 run.sh 脚本启动本地开发服务器，要求预先安装 Ollama 并拉取 llama3.2 模型，Ollama 须运行在默认地址 127.0.0.1:11434。代码仅在 Ubuntu 上测试过，采用 MIT 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Ollama 为 provider，调用本地 llama3.2 模型
- 代码高亮显示与一键复制代码片段
- 桌面与移动端自适应 UI
- run.sh 一键启动并自动打开浏览器

## 适用场景

- 在本地通过网页界面与 Llama 3.2 对话
- 提交问题并获取带语法高亮的代码回答
- 在 Ubuntu 机器上快速搭建本地 LLM 演示界面

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: LLaMa 3.2 Multimodal Web UI is a user-friendly interface for interacting with the Ollama platform. It effortlessly s
> L42: The application uses **Ollama as its provider** and sends requests to the local Ollama API using the `llama3.2` mod

## 星数曲线

```mermaid
xychart-beta
    title "iamgmujtaba/llama3.2-webUI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-31 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `87ab43cebff4` · [字段定义](../../DATASET.md)*
