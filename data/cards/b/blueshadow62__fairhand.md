# blueshadow62/fairhand

⭐ 7 · TypeScript · Apache-2.0 · 推送 2026-11-17 · [GitHub](https://github.com/blueshadow62/fairhand) · 个人维护

**教师用 AI 转录评分手写主观题答卷的桌面程序**

面向教师的 Electron 桌面应用：将扫描的手写论述题答卷 PDF 按题转录为文字，与答案表比对后生成 Excel 结果（成绩、题目分析、答案、答案表等信息表）。转录通过本机已安装的 Claude Code、Codex CLI 或 Anthropic/OpenAI/Gemini API 密钥完成，教师随后在复核界面逐题确认或修改判定。提供 Windows 安装包与 Mac beta dmg，内置无 AI 可用的示例集；README 明确 JBIG2/JPEG2000 压缩 PDF 可能分页失败。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 手写答卷 PDF 按题转录并与答案表比对生成 Excel 结果
- 支持 Claude Code/Codex 本地 CLI 登录或 Anthropic/OpenAI/Gemini API 密钥三种接入方式
- 按题分组复核界面，判定修改以案例形式批量应用到同答案的其他答卷
- 内置含预置转录的示例集，可在无 AI 环境下体验复核与 Excel 生成

## 适用场景

- 把学生手写论述题答卷扫描后批量转录并初步评分
- 在复核界面逐题核对 AI 判定并修正误转录的文字
- 生成含题目得分率与班级分数的 Excel 成绩表

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L5: 손글씨로 쓴 서·논술형 답안지(스캔 PDF)를 문항별 글자로 옮기고, 정답표와 비교해 엑셀로 정리하는 선생님용 프로그램입니다.
> L7: - 전사(손글씨 읽기)는 선생님 PC에 설치된 Claude Code·Codex(본인 구독 로그인)나 API 키(Anthropic·OpenAI·Gemini)로 합니다. 정확도는 AI 도구에 따라 다르며, 개발자

## 星数曲线

```mermaid
xychart-beta
    title "blueshadow62/fairhand 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-20"]
    y-axis "stars" 5 --> 8
    line [6, 7, 7]
```

2026-11-08 6 → 2026-11-20 7（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `8b66a436cb71` · [字段定义](../../DATASET.md)*
