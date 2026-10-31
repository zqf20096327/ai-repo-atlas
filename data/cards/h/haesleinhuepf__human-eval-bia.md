# haesleinhuepf/human-eval-bia

⭐ 26 · Jupyter Notebook · MIT · 推送 2026-06-03 · [GitHub](https://github.com/haesleinhuepf/human-eval-bia) · 个人维护

**评测 LLM 生成生物图像分析代码正确性的基准框架**

HumanEval 的 fork，将代码评测适配到生物图像分析领域：以 notebook 定义带 docstring 与 assert 单元测试的测试用例，向 LLM 发送提示生成 Python 代码，执行并统计 pass@k 通过率。作者用其比较了 15 个 LLM，支持 OpenAI、Google Gemini、Helmholtz blablador 与本地 Ollama 模型。程序会运行模型生成的不可信代码，执行调用默认被注释，需在沙箱中启用；商用模型运行会产生费用。用户新增测试用例时禁止使用 LLM 生成代码以避免偏置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- notebook 定义测试用例，含 docstring 提示与 assert 单元测试
- 支持 OpenAI、Gemini、blablador 与本地 Ollama 多种模型来源
- pass@k 通过率统计与按测试用例分组的可视化
- 对原版 HumanEval 的 Windows 兼容与文件系统测试等修改

## 适用场景

- 评测各 LLM 生成生物图像分析 Python 代码的功能正确性
- 比较多个 LLM 在生物图像分析任务上的通过率
- 按规范 notebook 格式扩展新的生物图像分析测试用例

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L10: Using the benchmark in this repository, we compared 15 LLMs in their capabilities to generate Bio-image Analysis Py
> L11: Therefore, we defined test-cases listed here which can be used to evaluate functional correctness of bio-image anal
> L65: To reproduce our benchmarks, you can go through the notebooks provided in the `/notebooks` directory:

## 星数曲线

```mermaid
xychart-beta
    title "haesleinhuepf/human-eval-bia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `1f9f76c26b60` · [字段定义](../../DATASET.md)*
