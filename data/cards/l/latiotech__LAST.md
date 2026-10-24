# latiotech/LAST

⭐ 184 · Python · GPL-3.0 · 推送 2026-05-28 · [GitHub](https://github.com/latiotech/LAST) · [官网](http://latio.tech/) · 组织维护

**CLI 代码安全扫描工具：用 OpenAI/Gemini 扫描安全与代码异味**

命令行 SAST 工具：用户自带 OpenAI 或 Gemini API key，扫描全量代码、变更文件或在 CI 流水线中运行，输出安全与代码健康问题；提供 partial/full 及 agentic 四种模式，agentic 模式用 AI agent 做更深入的分析并生成自动修复。默认模型 gpt-4o，可用 --model 切换。README 标注流水线功能目前不可用，Gemini 2.5 未测试。以 pip 安装的 Python 包分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 OpenAI 与 Gemini，用户自带 API key
- partial/full 与对应 agentic 四种扫描模式
- agentic 模式提供更深入分析与自动修复
- --health 选项聚焦代码优化建议

## 适用场景

- 合并前扫描变更文件的安全问题
- 对存量代码库做全量安全与健康扫描
- 在流水线中自动扫描变更（README 标注目前不可用）

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L11:  Use OpenAI or Gemini to scan your code for security and health issues from the CLI. Bring your own tokens. Options
> L34: 3. Scan only your changed files before merging with `latio partial /path/to/directory`. This uses the gpt-4o model 

## 星数曲线

```mermaid
xychart-beta
    title "latiotech/LAST 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 186 --> 188
    line [187, 187]
```

2026-10-18 187 → 2026-10-24 187（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `64446a3bcef9` · [字段定义](../../DATASET.md)*
