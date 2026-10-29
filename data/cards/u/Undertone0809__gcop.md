# Undertone0809/gcop

⭐ 196 · Python · MIT · 推送 2026-03-13 · [GitHub](https://github.com/Undertone0809/gcop) · [官网](https://gcop.zeeland.top) · 个人维护

**给开发者的 AI Git 提交信息生成与 Git 别名工具**

Python 编写的 Git 命令行助手：通过 git c / git ac 调用用户配置的 LLM（如 openai/gpt-4o）分析已暂存的改动并生成提交信息，用户以方向键选择后提交；可从仓库提交历史学习团队风格，支持自定义提交模板与提示词。另附 20+ 个 Git 别名（git undo、git p、git pf 等）。安装方式为 pip install gcop 后执行 gcop init 注入 Git 配置，需 Python 3.8+、Git 和 LLM API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- git c / git ac 生成 AI 提交信息并交互式选择
- 从仓库提交历史学习团队提交风格，支持自定义模板与提示词
- 20+ 个 Git 别名命令（undo、p、pf 等）
- 通过 config.yaml 配置任意 provider/name 格式的模型与 API key

## 适用场景

- 用 AI 生成符合团队风格的提交信息
- 用简短别名替代常用 Git 操作
- 按项目定制提交信息模板与规范

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L12: GCOP (Git Copilot) - Your AI-powered Git assistant that transforms messy commits into meaningful stories. It automa
> L122:    git c
> L141:    git ac

## 星数曲线

```mermaid
xychart-beta
    title "Undertone0809/gcop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 195 --> 197
    line [196, 196]
```

2026-10-18 196 → 2026-10-29 196（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2480983063d6` · [字段定义](../../DATASET.md)*
