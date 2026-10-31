# feiyun0112/Gradio.Net

⭐ 337 · C# · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/feiyun0112/Gradio.Net) · 个人维护 · 中文 README

**Gradio 的 .NET 移植：用 C# 几行代码为模型/API 构建 Web 界面**

将 Python 包 Gradio 6.30.0 移植到 .NET：把任意 C# 方法包装成 Web 页面，用户通过浏览器上传图片、输入文本、录音并与代码交互，无需编写 JavaScript/CSS。前端与协议复用 Python 版编译产物；提供 gr.Interface 快速封装与 gr.Blocks 布局控制两种 API 形态，名称与默认参数与 Python 版保持一致，移植仅需三类语法改动。附十个离线示例程序（聊天、流式、表单、媒体、多页、主题、图表等），可嵌入现有 ASP.NET Core 项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- gr.Interface 将 C# 方法直接包装为 Web 页面
- API 命名与 Python 版一致，移植仅需三类语法改动
- 可嵌入现有 ASP.NET Core 项目（AddGradio/UseGradio）
- 附十个离线示例程序，dotnet run 即可运行

## 适用场景

- 给 .NET 机器学习模型或 API 快速搭一个演示页面
- 把 Python Gradio 应用移植到 C#/.NET 技术栈
- 在现有 ASP.NET Core 项目中挂载模型交互页面

## 场景标签

 · 领域:机器学习工具/UI 组件

## 证据(README 行号)

> L5: Gradio for .NET — a port of Gradio 6.30.0, the Python package
> L9: With Gradio.Net you build a UI for a model, an API or any C# method in a few lines: users drag in


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c3387421f617` · [字段定义](../../DATASET.md)*
